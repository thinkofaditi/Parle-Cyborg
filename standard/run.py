import aiml
kernel=aiml.Kernel()
kernel.learn(".\\startup.xml")
kernel.respond("LOAD AIML B")
while True:
 print kernel.respond(raw_input("Enter your message >> "))
