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
urlShortenerText = font.render("URL Shortener",(0,0,0),True)

font=pygame.font.SysFont(None,30)

enterText=font.render("Paste your long URL below:",(0,0,0),True)

inputRect=pygame.Rect(50,240,630,40)
inputURL=pygame_gui.elements.UITextEntryLine(relative_rect=inputRect)

buttonRect=pygame.Rect(50,300,90,40)
button=pygame_gui.elements.UIButton(text="Generate",relative_rect=buttonRect)


shortenURLRect=pygame.Rect(50,390,630,40)

def url_Convert(inputURL):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(inputURL)
    print("The Shortened URL is: " + short_url)
    return short_url

clock=pygame.time.Clock()
while True:
    
    screen.fill((255,255,255))
    screen.blit(urlShortenerText,(250,50))
    screen.blit(enterText,(50,200))
          
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_RETURN:
                    url=url_Convert(inputURL.get_text())
                    pygame_gui.elements.UITextEntryLine(initial_text=url,relative_rect=shortenURLRect)
            except:
                pygame_gui.elements.UITextBox(relative_rect=shortenURLRect,html_text="Please enter a url")
        if event.type==pygame_gui.UI_BUTTON_PRESSED:
            try:
                if event.ui_element==button:
                    url=url_Convert(inputURL.get_text())
                    pygame_gui.elements.UITextEntryLine(initial_text=url,relative_rect=shortenURLRect)
            except:
                pygame_gui.elements.UITextBox(relative_rect=shortenURLRect,html_text="Please enter a url")
              
        manager.process_events(event)  
    manager.update(clock.tick(60)/1000)   
    manager.draw_ui(screen) 

                  
    pygame.display.update() 
