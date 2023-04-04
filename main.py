import pygame
x= pygame.init()
'init function helps to acess objects of the function pygame'
'Here we have declared an object gameWIndow using the given syntax which creates an window of size 1200*/500'
gameWindow= pygame.display.set_mode((1200,500))
pygame.display.set_caption("NEW")

'Set the icon for the game'
img = pygame.image.load('icon.jpg')
pygame.display.set_icon(img)

'Declaraing variables for the game'

exit_game= False
game_over= False

while not exit_gameas
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game= True
            'Exits the game on clicking on the close button'
        if event.type== pygame.KEYDOWN:
            'Loop to check whether the key is pressed'
            if(event.key== pygame.K_RIGHT):
                'Loop to check whether the right arrow key is pressed or not'
                print("You pressed right arrow")


pygame.quit()
quit()


