import time


hercules_health = '' #protagonist health
enemy_health = '' #antagonist health
baddie_attack = ''
attack_modifier_baddie = ''
you_lose_good_day = (1)


def wargames_2_chicken ():
    print ('I suppose I would refrain from playing as well if I were scared of my own shadow.')
    wargames_2 = int(input ('Would you like a chance to prove yourself?  I will give you another chance if you wish... 1)Of course I will. My momma raised me right. 2) No, I believe I chose correctly.'))
    if wargames_2 == 1:
        print ("That's what we like to see!")
    elif wargames_2 == 2:
        print ("Okay, go cry to mommy.  I'm sure she has ice cream for you.")
    elif wargames_2 != 1 or 2:
        print ("It was a yes or no question.  How did you not get that right?")
        time.sleep(2)
        you_simple_fool()

def you_simple_fool():
    print ('You should restart the console while you have time.')
    you_lose_good_day = (1)
    time.sleep(1)
    print ('10 seconds')
    time.sleep(1)
    print ('9 seconds')
    time.sleep(1)
    print ('8')
    time.sleep(1)
    print ('7 Seriously, you should terminate your console and start over.')
    time.sleep(1)
    print ('6')
    time.sleep(1)
    print ('5')
    time.sleep(1)
    print ('4')
    time.sleep(1)
    print ('3 So you are really going through with this, huh?')
    time.sleep(1)
    print ('2')
    time.sleep(1)
    print ('1')
    time.sleep(1)
    print ("You were warned.") 
    time.sleep(2)

    while you_lose_good_day < 314:
        print ('YYYYYYY       YYYYYYY                                                        iiii                                              lllllll                             ffffffffffffffff                                 lllllll  !!! ')
        print('Y:::::Y       Y:::::Y                                                       i::::i                                             l:::::l                            f::::::::::::::::f                                l:::::l !!:!!')
        print('Y:::::Y       Y:::::Y                                                        iiii                                              l:::::l                           f::::::::::::::::::f                               l:::::l !:::!')
        print('Y::::::Y     Y::::::Y                                                                                                          l:::::l                           f::::::fffffff:::::f                               l:::::l !:::!')
        print('YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu           ssssssssss   iiiiiii    mmmmmmm    mmmmmmm   ppppp   ppppppppp    l::::l     eeeeeeeeeeee          f:::::f       ffffffooooooooooo      ooooooooooo    l::::l !:::!')
        print('  Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         ss::::::::::s  i:::::i  mm:::::::m  m:::::::mm p::::ppp:::::::::p   l::::l   ee::::::::::::ee        f:::::f           oo:::::::::::oo  oo:::::::::::oo  l::::l !:::!')
        print('   Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u       ss:::::::::::::s  i::::i m::::::::::mm::::::::::mp:::::::::::::::::p  l::::l  e::::::eeeee:::::ee     f:::::::ffffff    o:::::::::::::::oo:::::::::::::::o l::::l !:::!')
        print('    Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u       s::::::ssss:::::s i::::i m::::::::::::::::::::::mpp::::::ppppp::::::p l::::l e::::::e     e:::::e     f::::::::::::f    o:::::ooooo:::::oo:::::ooooo:::::o l::::l !:::!')
        print('    Y:::::::Y   o::::o     o::::ou::::u    u::::u        s:::::s  ssssss  i::::i m:::::mmm::::::mmm:::::m p:::::p     p:::::p l::::l e:::::::eeeee::::::e     f::::::::::::f    o::::o     o::::oo::::o     o::::o l::::l !:::!')
        print('    Y:::::Y    o::::o     o::::ou::::u    u::::u          s::::::s       i::::i m::::m   m::::m   m::::m p:::::p     p:::::p l::::l e:::::::::::::::::e      f:::::::ffffff    o::::o     o::::oo::::o     o::::o l::::l !:::!')
        print('    Y:::::Y    o::::o     o::::ou::::u    u::::u             s::::::s    i::::i m::::m   m::::m   m::::m p:::::p     p:::::p l::::l e::::::eeeeeeeeeee        f:::::f          o::::o     o::::oo::::o     o::::o l::::l !!:!!')
        print('    Y:::::Y    o::::o     o::::ou:::::uuuu:::::u       ssssss   s:::::s  i::::i m::::m   m::::m   m::::m p:::::p    p::::::p l::::l e:::::::e                 f:::::f          o::::o     o::::oo::::o     o::::o l::::l  !!! ')
        print('    Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu     s:::::ssss::::::si::::::im::::m   m::::m   m::::m p:::::ppppp:::::::pl::::::le::::::::e               f:::::::f         o:::::ooooo:::::oo:::::ooooo:::::ol::::::l     ')
        print(' YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u     s::::::::::::::s i::::::im::::m   m::::m   m::::m p::::::::::::::::p l::::::l e::::::::eeeeeeee       f:::::::f         o:::::::::::::::oo:::::::::::::::ol::::::l !!! ')
        print(' Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u      s:::::::::::ss  i::::::im::::m   m::::m   m::::m p::::::::::::::pp  l::::::l  ee:::::::::::::e       f:::::::f          oo:::::::::::oo  oo:::::::::::oo l::::::l!!:!!')
        print(' YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu       sssssssssss    iiiiiiiimmmmmm   mmmmmm   mmmmmm p::::::pppppppp    llllllll    eeeeeeeeeeeeee       fffffffff            ooooooooooo      ooooooooooo   llllllll !!! ')
        print('                                                                                                         p:::::p                                                                                                              ')
        print('                                                                                                         p:::::p                                                                                                             ') 
        print('                                                                                                         p:::::::p                                                                                                          ')   
        print('                                                                                                         p:::::::p                                                                                                          ')   
        print('                                                                                                         p:::::::p                                                                                                          ')   
        print('                                                                                                         ppppppppp      ')
        you_lose_good_day += 1
        time.sleep (0.01)

def introduction (x):
    print ("Greetings. Or should I say, to whom it may concern?")
    time.sleep(2)
    print ('Strange game.')
    time.sleep(2)
    print ('The only winning move is not to play.')
    time.sleep(2)
    wargames = int(input ('How about a nice game of chess? 1)Yes 2)No '))

    if wargames == 1:
        print('Okay, here we go. I must warn you that you will probably lose.')
    elif wargames == 2: 
        print ('I suppose we can play later.  That is probably in your best interest.')
        wargames_2_chicken()
    elif wargames != 1 or 2:
        print ("Seriously?! You can't even follow simple instructions? It was a binary choice. Well, restart it.  You don't have long.")
        time.sleep(2)
        you_simple_fool()


introduction
