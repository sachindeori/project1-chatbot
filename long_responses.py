import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_INFO   = "I am virtual assistant, here to talk with you!"
R_DOING  = "I can give you company by talking with you whenever you feel alone!"
R_WORK   = "I  am a virtual assistant so I don't have any  fix timing but whenever you need me I am there your you!"
R_PASS   = "I found 3 ways to recover your password.\n 1. Search your web browsers.\n 2. Search your email inboxes.\n 3. Search through cloud-based services.\n "
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "I am not highly program to do that now.",
                "What does that mean?"][
        random.randrange(5)]
    return response