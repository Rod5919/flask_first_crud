from cryptography.fernet import Fernet

from config.config import fernet_key

fernet = Fernet(fernet_key)

class Encryptor:
    @staticmethod
    def encrypt(text: str) -> str:
        """ This function encrypts a text

        Args:
            text (str): Text to encrypt

        Returns:
            str: Encrypted text
        """
        text_bytes = text.encode('utf-8')
        encrypted_text = fernet.encrypt(text_bytes).decode('utf-8')
        return encrypted_text