import pygame

class Buttons:
    def __init__(self, text, screen, size_x=150, size_y=50, font="freesansbold.ttf", text_size=20,button_color ="gray",x_pos=0,y_pos=0, text_color="white", text_shadow = False, aliases = True, borders = False, line_thickness = 2, border_color = "red"):
        self.button_map = {
            "Size_X": size_x,
            "Size_Y": size_y,
            "Color": button_color,
            "Text": text,
            "Text_Size": text_size,
            "Text_Color": text_color,
            "Position_X": x_pos,
            "Position_Y": y_pos,
            "Font": font,
            "Screen": screen,
            "Text_Shadow": text_shadow,
            "aliases": aliases,
            "Borders": borders,
            "Line_Thickness": line_thickness,
            "Border_Color": border_color
        }
        self.font = pygame.font.Font(font, text_size)
        self.text = self.font.render(text, self.button_map["aliases"], text_color)
        self.shadow_text = self.font.render(text, self.button_map["aliases"], "black")
    def draw(self):
        if self.button_map["Borders"]:
            button_rect = pygame.rect.Rect(self.button_map["Position_X"]-self.button_map["Line_Thickness"], self.button_map["Position_Y"]-self.button_map["Line_Thickness"],
                                           self.button_map["Size_X"]+self.button_map["Line_Thickness"]*2, self.button_map["Size_Y"]+self.button_map["Line_Thickness"]*2)
            pygame.draw.rect(surface=self.button_map["Screen"], color=self.button_map["Border_Color"], rect=button_rect)

        button_rect = pygame.rect.Rect(self.button_map["Position_X"], self.button_map["Position_Y"], self.button_map["Size_X"], self.button_map["Size_Y"])
        pygame.draw.rect(surface=self.button_map["Screen"], color=self.button_map["Color"], rect=button_rect)
        if self.button_map["Text_Shadow"]:

            self.button_map["Screen"].blit(self.shadow_text,
                                           (self.button_map["Position_X"] + self.button_map["Size_X"] / 2 + 2,
                                            self.button_map["Position_Y"] + 12))
            self.button_map["Screen"].blit(self.text,
                                           (self.button_map["Position_X"] + self.button_map["Size_X"] / 2,
                                            self.button_map["Position_Y"] + 10))
        else:
            self.button_map["Screen"].blit(self.text,
                                           (self.button_map["Position_X"] + self.button_map["Size_X"] / 2,
                                            self.button_map["Position_Y"] + 10))
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_just_pressed()[0]:
            if self.button_map["Position_X"] < mouse_pos[0] < self.button_map["Size_X"] + self.button_map["Position_X"]:
                if self.button_map["Position_Y"] < mouse_pos[1] < self.button_map["Size_Y"] + self.button_map["Position_Y"]:
                    return True
        return False
    def text_shadow(self):
        self.text = self.font.render(self.button_map["Text"], self.button_map["aliases"], "black")

    def box_shadow(self):
        pass

