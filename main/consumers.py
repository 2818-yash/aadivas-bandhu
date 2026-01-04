import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from .models import SupportMessage


class SupportChatConsumer(WebsocketConsumer):

    def connect(self):
        user = self.scope["user"]

        if not user.is_authenticated:
            self.close()
            return

        self.room_group_name = "support_chat"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        # 🔹 SEND OLD MESSAGES ON CONNECT
        admin = User.objects.filter(is_superuser=True).first()
        if admin:
            messages = SupportMessage.objects.filter(
                sender__in=[user, admin],
                receiver__in=[user, admin]
            ).order_by("created_at")

            for msg in messages:
                self.send(text_data=json.dumps({
                    "sender": msg.sender.username,
                    "message": msg.message
                }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")
        sender = self.scope["user"]

        admin = User.objects.filter(is_superuser=True).first()
        if not admin:
            return

        # 🔹 SAVE MESSAGE ALWAYS (ADMIN ONLINE OR OFFLINE)
        SupportMessage.objects.create(
            sender=sender,
            receiver=admin,
            message=message
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "sender": sender.username,
                "message": message
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps({
            "sender": event["sender"],
            "message": event["message"]
        }))
