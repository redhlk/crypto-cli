import typer
from caesar_cipher import CaesarCipher

app = typer.Typer()


#Caesar cipher
caesar_app = typer.Typer()
app.add_typer(caesar_app, name="caesar")

@caesar_app.command()
def encrypt(message: str, shift: int):
    cipher = CaesarCipher(shift)
    encrypted_message = cipher.encrypt(message)
    typer.echo(encrypted_message)

@caesar_app.command()
def decrypt(message: str, shift: int):
    cipher = CaesarCipher(shift)
    decrypted_message = cipher.decrypt(message)
    typer.echo(decrypted_message)

@app.command()
def caesar_cipher():
    """
    Caesar Cipher tool
    """
    typer.echo("Use the 'encrypt' or 'decrypt' commands.")
def main():
    pass

if __name__ == "__main__":
    app()