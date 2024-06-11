import typer
from typing import Tuple
from typing_extensions import Annotated
from .caesar_cipher import CaesarCipher
from .rsa import encrypt as encrypt_rsa, decrypt as decrypt_rsa, generate_keypair
from .vigenere_cipher import VigenereCipher

app = typer.Typer()


# Caesar cipher
caesar_app = typer.Typer()
app.add_typer(caesar_app, name="caesar")


@caesar_app.command()
def encrypt(
    message: str,
    shift: Annotated[
        int, typer.Argument(help="The shift value you want to do the encription"),typer.Option(prompt=True)
    ] = 3,
):
    cipher = CaesarCipher(shift)
    encrypted_message = cipher.encrypt(message)
    typer.echo(encrypted_message)


@caesar_app.command()
def decrypt(message: str, shift: Annotated[int, typer.Argument()] = 3):
    cipher = CaesarCipher(shift)
    decrypted_message = cipher.decrypt(message)
    typer.echo(decrypted_message)


@app.command()
def caesar_cipher():
    """
    Caesar Cipher tool
    """
    typer.echo("Use the 'encrypt' or 'decrypt' commands.")


##RSA

rsa_app = typer.Typer()
app.add_typer(rsa_app, name="rsa")


@rsa_app.command()
def generate_key(
    p: Annotated[int, typer.Argument()] = 61, q: Annotated[int, typer.Argument()] = 53
):
    public, private = generate_keypair(p, q)
    print(f"Public Key: {public} and Private Key: {private}")


@rsa_app.command()
def encrypt(
    message: str, pk: Annotated[Tuple[int, int], typer.Argument(help="Public key")]
):

    cipher = encrypt_rsa(pk, message)
    typer.echo(cipher)


@rsa_app.command()
def decrypt(
    message: str, pk: Annotated[Tuple[int, int], typer.Argument(help="Private key")]
):

    cipher = decrypt_rsa(pk, message)
    typer.echo(cipher)


##vigenere

vigenere_app = typer.Typer()
app.add_typer(vigenere_app, name="vigenere")


@vigenere_app.command()
def encrypt(
    message: str,
    key: Annotated[str, typer.Argument(help="Key")] = "KEY",
):
    cipher = VigenereCipher(key=key)
    encrypted_message = cipher.encrypt(message)
    typer.echo(encrypted_message)


@vigenere_app.command()
def decrypt(
    message: str,
    key: Annotated[str, typer.Argument(help="Key")] = "KEY",
):
    cipher = VigenereCipher(key)
    decrypted_message = cipher.decrypt(message)
    typer.echo(decrypted_message)


def main():
    print("main in the src file called..")
    pass


if __name__ == "__main__":
    app()
