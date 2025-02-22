import pyshorteners
import pygame
import sys
import pygame_gui

pygame.init()

screen=pygame.display.set_mode((800,600))
manager=pygame_gui.UIManager((800,600))

pygame.display.set_caption("URL Shortener")
icon=pygame.image.load("./urlIcon.png")
pygame.display.set_icon(icon)

font=pygame.font.SysFont(None,60)
urlShortenerText = font.render("URL Shortener",True,(0,0,0))

font=pygame.font.SysFont(None,30)
enterText=font.render("Paste your long URL below:",True,(0,0,0))

inputRect=pygame.Rect(50,240,630,40)
inputURL=pygame_gui.elements.UITextEntryLine(relative_rect=inputRect, manager=manager)

buttonRect=pygame.Rect(50,300,90,40)
button=pygame_gui.elements.UIButton(text="Generate",relative_rect=buttonRect, manager=manager)

shortenURLRect=pygame.Rect(50,390,630,40)
shortenURLLabel = pygame_gui.elements.UITextBox(relative_rect=shortenURLRect, html_text="", manager=manager)

def url_Convert(inputURL):
    try:
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(inputURL)
        print("The Shortened URL is: " + short_url)
        return short_url
    except:
        return "Invalid URL"

clock=pygame.time.Clock()
while True:
    screen.fill((255,255,255))
    screen.blit(urlShortenerText,(250,50))
    screen.blit(enterText,(50,200))
          
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                shortened_url = url_Convert(inputURL.get_text())
                shortenURLLabel.set_text(shortened_url)
        manager.process_events(event)  
    manager.update(clock.tick(60)/1000)   
    manager.draw_ui(screen) 
    pygame.display.update()
