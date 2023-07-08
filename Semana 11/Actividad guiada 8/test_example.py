def admin_command(command, sudo=True):
    if sudo:
        return ["Feliz"] + command
    return command

def test_admin_command():
    assert admin_command("algo") == ["Feliz", "algo"]