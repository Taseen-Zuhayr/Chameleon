import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Color changing sprite')

    colors = {
                'default': pygame.Color('white'),
                'blue': pygame.Color('blue'),
                'yellow': pygame.Color('yellow'),
                'red': pygame.Color('red'),
                'green': pygame.Color('green'),
    }
    x, y, size = 30, 30, 60
    color = colors['default']
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        keys = pygame.key.get_pressed()
        x += (keys[pygame.K_d] - keys[pygame.K_a]) * 3
        y += (keys[pygame.K_s] - keys[pygame.K_w]) * 3
        x, y = max(0, min(440, x)), max(0, min(440,y))

        color = (
                    colors['blue'] if x == 0 else
                    colors['yellow'] if x == 440 else
                    colors['red'] if y == 0 else
                    colors['green'] if y == 440 else
                    colors['default']
        )

        screen.fill((0,0,0))
        pygame.draw.rect(screen,color,(x,y,size,size))
        pygame.display.flip()
        clock.tick(90)

if __name__ == "__main__":
    main()
