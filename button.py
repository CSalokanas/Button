import pygame

class Buttons:
    def __init__(self, text, screen, size_x=150, size_y=50, font="freesansbold.ttf", text_size=20,button_color ="gray",x_pos=0,y_pos=0, text_color="black"):
        self.font = pygame.font.Font(font, text_size)
        self.text = text
        self.text = self.font.render(text, True, color=text_color)
        self.x = x_pos
        self.y = y_pos
        self.screen = screen
        self.size_x = size_x
        self.size_y = size_y
        self.button_color = button_color

    def draw(self):
        button_rect = pygame.rect.Rect(self.x, self.y, self.size_x, self.size_y)
        pygame.draw.rect(surface=self.screen, color=self.button_color, rect=button_rect)
        self.screen.blit(self.text, (self.x + 10, self.y + 10))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.x < mouse_pos[0] < self.x + self.size_x:
                if self.y < mouse_pos[1] < self.y + self.size_y:
                    return True
        return False
