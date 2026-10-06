import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from circleshape import CircleShape
from shot import Shot




def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    font = pygame.font.Font(None, 36)
   
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score=0
    game_over = False
    
    while True:
        log_state()
        screen.fill("black")
        score_surface = font.render(f"Score: {score}", True, "white")
        screen.blit(score_surface, (10, 10))

        if not game_over:
            for obj in drawable:
                obj.draw(screen)

            updatable.update(dt)
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    print("Game over!")
                
                    game_over = True

            for asteroid in asteroids:
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        shot.kill()
                        asteroid.split()
                        score+=1
        else:
            game_over_text = font.render("GAME OVER", True, "red")
            retry_text = font.render("Press R to retry", True, "white")
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
            retry_rect = retry_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))

            screen.blit(game_over_text, game_over_rect)
            screen.blit(retry_text, retry_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game_over = False
                score = 0
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        dt =clock.tick(60) / 1000 
            
        
        pygame.display.flip()


        
                   

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
