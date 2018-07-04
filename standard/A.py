import aiml
kernel=aiml.Kernel()
kernel.learn("F:\\minerva\\aiml-0.8.6\\aiml\\standard\\startup.xml")
kernel.respond("LOAD AIML B")
while True:
 print kernel.respond(raw_input("Enter your message >> "))
