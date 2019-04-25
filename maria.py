#Maria's exercise to practice if statements
cookies = raw_input ("How many cookies have you had so far? ")
cookies = int(cookies)

def can_have_cookies(cookies):
    if cookies >= 3:
        print "you've had too many cookies"
    else:
        print "you can have one more cookie"

can_have_cookies(cookies)
