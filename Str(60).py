# MY GAME
import pygame
import time
import random

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
YELLOW = (255, 255,   0)

pygame.init()

# Set the width and height of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Str(60)")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
"""PREREQS"""
soundOff = False
pygame.mixer.music.load("SFV Concept AlbumSpectral Assassin Nash SFA RMX.mp3")
pygame.mixer.music.play(-1)


class mySprite(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("UserSprite.png")
        self.rect = self.image.get_rect()
        self.lives = 3


userSprite = mySprite()

allProjectiles = pygame.sprite.RenderPlain()


class projectile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Projectile.png")
        self.rect = self.image.get_rect()
        self.rect.top = 500
        self.rect.right = 0
        self.direction = 0, -7


def getMultipleChoiceQuestions():
    questionsList = {}
    myFile = open("Str(60)Questions.txt", "r")
    allData = myFile.read()
    data = allData.split("\n")

    for i in range(0, len(data), 5):
        questionsList.update({data[i]: data[i+1:i+5]})

    return questionsList


questionsList = getMultipleChoiceQuestions()

randomQuestion = "Blank"
chosen = 0


def evaluateAnswer(chosen, questionsList, randomQuestion, allChoices):
    for i in range(4):
        if allChoices[i] == questionsList[randomQuestion][0]:
            correct = pygame.sprite.Sprite()
            correct.image = pygame.image.load("correct.png")
            screen.blit(correct.image, [575, 180+(i*75)])
            pygame.display.update()
        else:
            incorrect = pygame.sprite.Sprite()
            incorrect.image = pygame.image.load("incorrect.png")
            screen.blit(incorrect.image, [575, 180+(i*75)])
            pygame.display.update()

    time.sleep(3)
    if questionsList[randomQuestion][0] != allChoices[chosen-1]:
        userSprite.lives -= 1
    del questionsList[randomQuestion]
    randomQuestion = "Blank"
    allChoices = []
    return randomQuestion, allChoices, questionsList


questionStart = 0
questionEnd = 0

difficulties = [5, 3, 2]

currentScreen = "menuScreen"
"""PREREQS END"""
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if (event.type == pygame.KEYDOWN):  # KEYDOWN means a key is pressed
            if (event.key == pygame.K_SPACE):
                userSprite.lives = 3
        if currentScreen == "menuScreen":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Prevents user from selecting input while holding down mouse button
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    mouseLocation = pygame.mouse.get_pos()
                    if mouseLocation[0] >= 600 and mouseLocation[0] <= 650 and mouseLocation[1] >= 50 and mouseLocation[1] <= 100:
                        # Quit Button Pressed
                        done = True
                    elif mouseLocation[0] >= 50 and mouseLocation[0] <= 100 and mouseLocation[1] >= 400 and mouseLocation[1] <= 450:
                        # Music Button Pressed
                        if not soundOff:
                            pygame.mixer.music.pause()
                            soundOff = True
                        else:
                            pygame.mixer.music.unpause()
                            soundOff = False
                    elif mouseLocation[0] >= 200 and mouseLocation[0] <= 500 and mouseLocation[1] >= 200 and mouseLocation[1] <= 350:
                        # Play Button Pressed
                        userSprite.lives = 3
                        stage = 1
                        timeLeft = 60
                        startTime = time.strftime("%S")
                        questionStart = 0
                        questionEnd = 0
                        spawned = []
                        projectileTimerStart = time.strftime("%S")
                        allProjectiles.empty()
                        currentScreen = "playScreen"
                    elif mouseLocation[0] >= 250 and mouseLocation[0] <= 450 and mouseLocation[1] >= 375 and mouseLocation[1] <= 450:
                        # Play Button Pressed
                        currentScreen = "optionsScreen"
        elif currentScreen == "optionsScreen":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Prevents user from selecting input while holding down mouse button
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    mouseLocation = pygame.mouse.get_pos()
                    if mouseLocation[0] >= 600 and mouseLocation[0] <= 650 and mouseLocation[1] >= 50 and mouseLocation[1] <= 100:
                        # Close Button Pressed
                        currentScreen = "menuScreen"
                    elif mouseLocation[0] >= 50 and mouseLocation[0] <= 100 and mouseLocation[1] >= 400 and mouseLocation[1] <= 450:
                        # Music Button Pressed
                        if not soundOff:
                            pygame.mixer.music.pause()
                            soundOff = True
                        else:
                            pygame.mixer.music.unpause()
                            soundOff = False
        elif currentScreen == "playScreen":
            pass
        elif currentScreen == "questionScreen":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Prevents user from selecting input while holding down mouse button
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    mouseLocation = pygame.mouse.get_pos()
                    if mouseLocation[0] >= 200 and mouseLocation[0] <= 550 and mouseLocation[1] >= 175 and mouseLocation[1] <= 225:
                        # Choice1 Button Pressed
                        randomQuestion, allChoices, questionsList = evaluateAnswer(
                            1, questionsList, randomQuestion, allChoices)
                        stage += 1
                        timeLeft -= 1
                        questionEnd = time.time()
                        projectileTimerStart = time.strftime("%S")
                        currentScreen = "playScreen"
                    elif mouseLocation[0] >= 200 and mouseLocation[0] <= 550 and mouseLocation[1] >= 250 and mouseLocation[1] <= 300:
                        # Choice2 Button Pressed
                        randomQuestion, allChoices, questionsList = evaluateAnswer(
                            2, questionsList, randomQuestion, allChoices)
                        stage += 1
                        timeLeft -= 1
                        questionEnd = time.time()
                        projectileTimerStart = time.strftime("%S")
                        currentScreen = "playScreen"
                    elif mouseLocation[0] >= 200 and mouseLocation[0] <= 550 and mouseLocation[1] >= 325 and mouseLocation[1] <= 375:
                        # Choice3 Button Pressed
                        randomQuestion, allChoices, questionsList = evaluateAnswer(
                            3, questionsList, randomQuestion, allChoices)
                        stage += 1
                        timeLeft -= 1
                        questionEnd = time.time()
                        projectileTimerStart = time.strftime("%S")
                        currentScreen = "playScreen"
                    elif mouseLocation[0] >= 200 and mouseLocation[0] <= 550 and mouseLocation[1] >= 400 and mouseLocation[1] <= 450:
                        # Choice4 Button Pressed
                        randomQuestion, allChoices, questionsList = evaluateAnswer(
                            4, questionsList, randomQuestion, allChoices)
                        stage += 1
                        timeLeft -= 1
                        questionEnd = time.time()
                        projectileTimerStart = time.strftime("%S")
                        currentScreen = "playScreen"
                    elif mouseLocation[0] >= 50 and mouseLocation[0] <= 100 and mouseLocation[1] >= 400 and mouseLocation[1] <= 450:
                        # Music Button Pressed
                        if not soundOff:
                            pygame.mixer.music.pause()
                            soundOff = True
                        else:
                            pygame.mixer.music.unpause()
                            soundOff = False

        elif currentScreen == "winScreen" or currentScreen == "loseScreen":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Prevents user from selecting input while holding down mouse button
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    mouseLocation = pygame.mouse.get_pos()
                    if mouseLocation[0] >= 175 and mouseLocation[0] <= 525 and mouseLocation[1] >= 250 and mouseLocation[1] <= 350:
                        # PLAY AGAIN Button Pressed
                        currentScreen = "menuScreen"
                    elif mouseLocation[0] >= 250 and mouseLocation[0] <= 450 and mouseLocation[1] >= 375 and mouseLocation[1] <= 450:
                        # QUIT Button Pressed
                        done = True

        if (event.type == pygame.KEYDOWN):  # KEYDOWN means a key is pressed
            if (event.key == pygame.K_UP):
                print(pygame.mouse.get_pos())

    if currentScreen == "menuScreen":
        screenDisplyed = pygame.image.load("startScreen.png")
        screen.blit(screenDisplyed, [0, 0])

    if currentScreen == "playScreen":
        if userSprite.lives == 0:
            currentScreen = "loseScreen"
        elif stage == 4:
            currentScreen = "winScreen"
        else:
            screenDisplyed = pygame.image.load("playScreen.png")
            screen.blit(screenDisplyed, [0, 0])

            userSprite.rect.center = pygame.mouse.get_pos()
            screen.blit(userSprite.image, userSprite.rect)
            time.sleep(0.0001)

            difficulty = difficulties[stage-1]

            def spawnWave(size, allProjectiles):
                hole = random.randrange(0, 650, 50)
                for i in range(int(size[0]/50)):
                    currentProjectile = projectile()
                    currentProjectile.rect.left = i*50
                    if currentProjectile.rect.left == hole or currentProjectile.rect.left == hole+50:
                        currentProjectile.rect.right = 0
                    allProjectiles.add(currentProjectile)
                return allProjectiles

            projectileTimerEnd = time.strftime("%S")

            if int(projectileTimerEnd) < int(projectileTimerStart):
                projectileTimerEnd = int(projectileTimerEnd)+60
            if int(projectileTimerEnd)-int(projectileTimerStart) == difficulty:
                spawnWave(size, allProjectiles)
                projectileTimerStart = projectileTimerEnd

            for item in allProjectiles:
                if (pygame.sprite.collide_rect(userSprite, item)):
                    userSprite.lives -= 1
                    item.rect.topright = (0, 500)
                item.rect = item.rect.move(item.direction)

            allProjectiles.draw(screen)

            playerBar = pygame.sprite.Sprite()
            playerBar.image = pygame.image.load("playerBar.png")
            screen.blit(playerBar.image, [50, 50])

            timer = pygame.sprite.Sprite()
            timer.image = pygame.image.load("timer.png")
            screen.blit(timer.image, [550, 50])

            questionTime = questionEnd-questionStart
            timeLeft += questionTime
            timeLeft = int(timeLeft)

            endTimer = time.strftime("%S")
            if endTimer < startTime:
                timeLeft -= 60
            timeLeft -= (int(endTimer)-int(startTime))
            startTime = endTimer

            myFont = pygame.font.Font(None, 70)
            text = myFont.render(str(timeLeft), True, WHITE)
            if len(str(timeLeft)) == 2:
                screen.blit(text, [572, 77])
            elif len(str(timeLeft)) == 1:
                screen.blit(text, [585, 77])

            if timeLeft in [40, 20, 0]:
                currentScreen = "questionScreen"
                allProjectiles.empty()
                questionStart = time.time()
            else:
                questionStart = 0
                questionEnd = 0

            playerLogo = pygame.sprite.Sprite()
            playerLogo.image = pygame.image.load("playerLogo.png")
            screen.blit(playerLogo.image, [64, 64])

            def playerStatus(stage):
                livesColour = [RED, YELLOW, GREEN]
                livesColour = livesColour[userSprite.lives-1]

                pygame.draw.rect(screen, livesColour, [
                                 199, 64, 38*userSprite.lives, 33])
                pygame.draw.rect(screen, BLACK, [199, 64, 38, 33], 1)
                if userSprite.lives > 1:
                    pygame.draw.rect(screen, BLACK, [199, 64, 76, 33], 1)
                if userSprite.lives > 2:
                    pygame.draw.rect(screen, BLACK, [199, 64, 114, 33], 1)

                myFont = pygame.font.Font(None, 35)
                text = myFont.render(str(stage), True, WHITE)
                screen.blit(text, [220, 108])

            if userSprite.lives > 0:
                playerStatus(stage)

            pygame.display.update()

    if currentScreen == "optionsScreen":
        screenDisplyed = pygame.image.load("optionsScreen.png")
        screen.blit(screenDisplyed, [0, 0])

    if currentScreen == "questionScreen":
        if randomQuestion == "Blank":
            screenDisplyed = pygame.image.load("questionScreen.png")
            screen.blit(screenDisplyed, [0, 0])

            allChoices = []
            randomQuestion = list(questionsList.keys())[
                random.randint(0, (len(questionsList)-1))]
            str(randomQuestion)
            myFont = pygame.font.Font(None, 15)
            text = myFont.render(randomQuestion, True, WHITE)
            screen.blit(text, [175, 73])

            def blitChoice(choice, ylocation):
                text = myFont.render(choice, True, WHITE)
                screen.blit(text, (266, ylocation))
                return choice

            if randomQuestion == "Which pygame operation is used to create a quarter circle?" or randomQuestion == "What Is the correct format for an EasyGui message box?":
                myFont = pygame.font.Font(None, 13)
            else:
                myFont = pygame.font.Font(None, 25)

            randomOrder = list(range(4))
            random.shuffle(randomOrder)

            for number in randomOrder:
                allChoices.append(blitChoice(
                    questionsList[randomQuestion][number], 200+(randomOrder.index(number)*73)))

    if currentScreen == "winScreen":
        screenDisplyed = pygame.image.load("winScreen.png")
        screen.fill(BLACK)
        screen.blit(screenDisplyed, [0, 0])

    if currentScreen == "loseScreen":
        screenDisplyed = pygame.image.load("loseScreen.png")
        screen.fill(BLACK)
        screen.blit(screenDisplyed, [0, 0])

    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
