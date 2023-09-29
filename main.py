
import pygame as pg
import moderngl
import sys
import pygame.time

from model import *

class GraphicsEngine:
    def __init__(self, win_size=(800,400)):
        # init pygame
        pygame.init()
        # window size
        self.WIN_SIZE = win_size
        # opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE,flags=pygame.OPENGL | pygame.DOUBLEBUF)
        # use existing opngl context
        self.ctx = moderngl.create_context()
        # create an object for time tracking
        self.cloak = pygame.time.Clock()
        #scene
        self.scene=Triangle(self)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.scene.destroy()
                pygame.quit()
                sys.exit()
    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        #scene
        self.scene.render()
        # swap buffer
        pygame.display.flip()
    def run(self):
        while True:
            self.check_events()
            self.render()
            self.cloak.tick(60)


if __name__=='__main__':
    app = GraphicsEngine()
    app.run()