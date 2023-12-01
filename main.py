import pygame


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    running = True
    while running:  # главный игровой цикл
        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # обработка остальных событий
        # отрисовка изменений
        # обновить экран
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
