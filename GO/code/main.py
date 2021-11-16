#Main Menu

#libraries
import pygame, sys, os


def run():
    print('this is running')


class Button:
    def __init__(self, image, position, callback):
        self.image = pygame.image.load(image)
        self.image.convert()
        self.rect = self.image.get_rect(topleft=position)
        self.callback = callback
 
    def on_click(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

script_dir = sys.path[0]
img_path = os.path.join(script_dir, '../info/images/background.png')
(width, height) = (1200, 750)
bg = pygame.image.load(img_path)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Main Menu')
btn = Button('test.png', (30,30), run)

def mainloop():
    
    while True:
        
        screen.blit(bg, (0, 0))
        screen.blit(btn.image, btn.rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                btn.on_click(event)
            
        
        pygame.display.update()



mainloop()


