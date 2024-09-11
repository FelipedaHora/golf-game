import pygame

class Animation:
    def __init__(self, sprite_sheet_path, frame_width, frame_height, frame_count, frame_duration):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_count = frame_count
        self.frame_duration = frame_duration
        self.frames = self.load_frames()
        self.current_frame = 0
        self.time_accumulated = 0

    def load_frames(self):
        frames = []
        for i in range(self.frame_count):
            frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
            frame.blit(self.sprite_sheet, (0, 0), (i * self.frame_width, 0, self.frame_width, self.frame_height))
            frames.append(frame)
        return frames

    def update(self, delta_time):
        self.time_accumulated += delta_time
        if self.time_accumulated >= self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.time_accumulated = 0

    def draw(self, screen, position):
        screen.blit(self.frames[self.current_frame], position)

    def reset(self):
        self.current_frame = 0
        self.time_accumulated = 0