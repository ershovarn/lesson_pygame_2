import pygame


def draw_circle(screen: pygame.Surface, coords_centre):
    pygame.draw.circle(screen, pygame.Color('red'),
                       coords_centre, 20)


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    x, y = 0, height // 2
    v = 20
    do_paint = False
    running = True
    while running:  # главный игровой цикл
        # цикл обработки событий

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and do_paint:
                coords_mouse = event.pos
                # print(coords_mouse)
                # screen.fill((0, 0, 0))
                draw_circle(screen, coords_mouse)
            if event.type == pygame.MOUSEBUTTONDOWN:
                do_paint = True
            if event.type == pygame.MOUSEBUTTONUP:
                do_paint = False
            # обработка остальных событий
        # отрисовка изменений
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
