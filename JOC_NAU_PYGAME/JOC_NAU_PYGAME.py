
import pygame
import random
import sys
import math

# ========================
# Configuració inicial
# ========================
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255,255,0)
AMARILLO_LIMA = (50, 205, 50)

# Inicialitzar Pygame, el mixer per la música i sons i la finestra
pygame.init()
pygame.mixer.init()

# Inicialitzem les pistes d'audio (música i sons)
pista_menus = "pistamenus.mp3"
pista_ingame = "pistaingame.mp3"
canal_menus = pygame.mixer.Channel(0)
canal_ingame = pygame.mixer.Channel(1)
canal_menus.set_volume(0.8)
canal_ingame.set_volume(0.8)


efecte_colisio = pygame.mixer.Sound("pistagettinghit.wav")
efecte_powerup = pygame.mixer.Sound("pistapowerup.wav")
efecte_tret = pygame.mixer.Sound("pista_disparo.wav")
efecte_pausa = pygame.mixer.Sound("PauseSound.wav")
efecte_reanudar = pygame.mixer.Sound("UnpauseSound.wav")
efecte_healup = pygame.mixer.Sound("Efecte_heal_up.mp3")
efecte_destruccio_roca = pygame.mixer.Sound("efecte_destruccio_roca.mp3")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE WARS - PYGAME")
clock = pygame.time.Clock()
font_standard = pygame.font.SysFont("Arial", 24)
font_pause = pygame.font.SysFont("Impact", 90)
font_menu_titol = pygame.font.SysFont("Courier New", 90)
font_menu_titol.set_bold(True) #Activar negreta i subratllat de font_menu_titol
font_menu_titol.set_underline(True)
font_menu_text = pygame.font.SysFont("Courier New", 30)
font_menu_text.set_bold(True) #Activar negreta de font_menu_text
font_powerups = pygame.font.SysFont("Impact", 30)
font_powerups.set_italic(True)

background = pygame.image.load("ImatgeMenu.webp")
background2 = pygame.image.load("possiblefondo.jpg")
background3 = pygame.image.load("pause_background.jpg")
background4 = pygame.image.load("Espacio_fondo.jpg")

# ========================
# Variables Globals del Joc
# ========================
score = 0
difficulty_level = 1
lives = 3
last_difficulty_update_time = pygame.time.get_ticks()
spawn_interval = 1500
ADD_OBSTACLE = pygame.USEREVENT + 1
ADD_POWERUP =  pygame.USEREVENT + 2
SPEED_BOOST = pygame.USEREVENT + 3
ADD_HEALING = pygame.USEREVENT + 4
pausado = False
max_score = 0
powerup_message = ""
powerup_message_time = 0


# ========================
# Funcions Auxiliars
# ========================

def draw_text(surface, text, font_standard, color, x, y):
    """Dibuixa un text a la pantalla."""
    text_obj = font_standard.render(text, True, color)
    surface.blit(text_obj, (x, y))

def play_music(track, loop = -1):
    pygame.mixer.music.load(track)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loop)

def add_life():
    global lives
    lives += 1

# ========================
# Classes del Joc
# ========================

class Player(pygame.sprite.Sprite):
    """Classe per al jugador."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load("Nau_joc.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.base_speed = 5
        self.speed = self.base_speed

    def update(self):
        """Actualitza la posició del jugador segons les tecles premudes i reprodueix so de moviment"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


        # Evitar que el jugador surti de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def increase_speed(self):
        self.speed = self.base_speed + 3
        pygame.time.set_timer(SPEED_BOOST, 3500, loops=1)

    def shoot(self):
        """Dispara una bala desde la posició del jugador"""
        bullet = Bullet(self.rect.right, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Obstacle(pygame.sprite.Sprite):
    """Classe per als obstacles."""

    def __init__(self):
        super().__init__()
        self.obstacle_meteorit = pygame.image.load("Obstacle_meteorit.png")
        self.explosio_meteorit = pygame.image.load("explosion.png")
        # Crear un obstacle amb dimensions aleatòries
        width = random.randint(70, 100)
        height = random.randint(70, 100)

        original_size = self.obstacle_meteorit.get_size()

        # Escalar manteniendo la proporción
        scale_factor = min(width / original_size[0], height / original_size[1])
        new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))

        # Redimensionar la imagen sin deformar
        self.image = pygame.transform.scale(self.obstacle_meteorit, new_size)

        self.rect = self.image.get_rect()
        # Posició inicial: fora de la pantalla per la dreta
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, HEIGHT - new_size[1])
        # La velocitat s'incrementa amb la dificultat
        self.speed = random.randint(7 + difficulty_level, 15 + difficulty_level)

    def update(self):
        """Actualitza la posició de l'obstacle movent-lo cap a l'esquerra.
           Quan surt completament de la pantalla, s'incrementa la puntuació i s'elimina."""
        global score
        self.rect.x -= self.speed
        if self.rect.right < 0:
            score +=1
            self.kill()

class Powerup(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #Creem el PowerUp
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load("Imatge_speed_boost.png")
        self.rect = self.image.get_rect()
        # Posició inicial: fora de la pantalla per la dreta
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, 500)
        # La velocitat s'incrementa amb la dificultat
        self.speed = random.randint(2 + difficulty_level, 10 + difficulty_level)

    def update(self):
        """Actualitza la posició de l'obstacle movent-lo cap a l'esquerra.
           Quan surt completament de la pantalla s'elimina."""
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((14, 5))  # Tamaño de la bala
        self.image.fill(AMARILLO_LIMA)  # Color de la bala
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10  # Velocidad de la bala

    def update(self):
        """Mover la bala hacia la derecha y eliminarla si sale de la pantalla"""
        self.rect.x += self.speed
        if self.rect.left > WIDTH:  # Si sale de la pantalla, se elimina
            self.kill()

class Healing(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #Creem el Healing
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load("Imatge_vida.png")
        self.rect = self.image.get_rect() 
        # Posició inicial: fora de la pantalla per la dreta
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, 500)
        # La velocitat s'incrementa amb la dificultat
        self.speed = random.randint(1 + difficulty_level, 6 + difficulty_level)
        self.time = 0

    def update(self):
        """Actualitza la posició de l'obstacle movent-lo cap a l'esquerra.
           Quan surt completament de la pantalla s'elimina."""

        self.rect.x -= self.speed

        # Movimiento en forma de "S" (usamos la función seno)
        self.rect.y += math.sin(self.time) * 6  # Movimiento en Y con la función seno
        self.time += 0.1  # Incrementamos el tiempo para cambiar el valor de seno

        if self.rect.right < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("explosion.png")  # Carrega la imatge de l'explosió
        self.image = pygame.transform.scale(self.image, (50, 50))  # Escalar la imatge
        self.rect = self.image.get_rect(center=(x, y))
        self.timer = pygame.time.get_ticks()  # Guarda el temps d'inici de l'explosió

    def update(self):
        """Eliminar l'explosió després de 500ms"""
        if pygame.time.get_ticks() - self.timer > 500:
            self.kill()

# ========================
# Funció per reinicialitzar el Joc
# ========================

def new_game():
    """Reinicialitza totes les variables i grups per començar una nova partida."""
    global score, difficulty_level, lives, last_difficulty_update_time, spawn_obstacle_interval, all_sprites, obstacles, player, powerups, spawn_powerup_interval,bullets,healings,spawn_healing_interval, explosio_meteorit
    score = 0
    difficulty_level = 1
    lives = 3
    last_difficulty_update_time = pygame.time.get_ticks()
    spawn_obstacle_interval = 1000
    spawn_powerup_interval = 5000
    spawn_healing_interval = 10000
    pygame.time.set_timer(ADD_OBSTACLE, spawn_obstacle_interval)
    pygame.time.set_timer(ADD_POWERUP, spawn_powerup_interval )
    pygame.time.set_timer(ADD_HEALING, spawn_healing_interval)
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    healings = pygame.sprite.Group()
    explosio_meteorit = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)


# ========================
# Funció per mostrar el menú principal
# ========================

def show_menu():
    """Mostra la pantalla de menú d'inici i espera que l'usuari premi alguna tecla per començar."""
    play_music(pista_menus)
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        screen.blit(background, (0,0))
        draw_text(screen, "Space Wars", font_menu_titol, YELLOW, 140, 100)
        draw_text(screen, "Prem qualsevol tecla per començar", font_menu_text, YELLOW, 100, 295)
        draw_text(screen, "Controls :arrow keys,spacebar per disparar", font_menu_text, BLACK, 20, 400)

        pygame.display.flip()


# ========================
# Funció per executar la partida
# ========================

def game_loop():
    """Executa el bucle principal de la partida."""
    global difficulty_level, last_difficulty_update_time, spawn_interval, lives,score,pausado,max_score,healing,powerup_message_time,powerup_message
    new_game()
    play_music(pista_ingame)
    game_state = "playing"
    running = True
    while running and game_state == "playing":
        clock.tick(FPS)
        screen.blit(background2, (0, 0))
        all_sprites.draw(screen)
        max_score_text = font_standard.render("Puntuació Màxima: " + str(max_score), True, YELLOW)
        score_text = font_standard.render("Puntuació: " + str(score), True, YELLOW)
        difficulty_text = font_standard.render("Dificultat: " + str(difficulty_level), True, YELLOW)
        lives_text = font_standard.render("Vides: " + str(lives), True, YELLOW)
        speed_text = font_standard.render("Velocitat: " + str(player.speed), True, YELLOW)
        screen.blit(max_score_text, (10, 10))
        screen.blit(score_text, (10, 40))
        screen.blit(difficulty_text, (10, 70))
        screen.blit(lives_text, (10, 100))
        screen.blit(speed_text, (10, 130))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == ADD_OBSTACLE and not pausado:
                obstacle = Obstacle()
                all_sprites.add(obstacle)
                obstacles.add(obstacle)
            elif event.type == ADD_POWERUP and not pausado:
                powerup = Powerup()
                all_sprites.add(powerup)
                powerups.add(powerup)
            elif event.type == ADD_HEALING and not pausado:
                healing = Healing()
                all_sprites.add(healing)
                healings.add(healing)
            elif event.type == SPEED_BOOST:
                player.speed = player.base_speed
            elif event.type == pygame.KEYDOWN:
                all_sprites.add(bullets)
                bullets.add(bullets)
                if event.key == pygame.K_SPACE:
                    efecte_tret.play()
                    efecte_tret.set_volume(0.1)
                    player.shoot()
                elif event.key == pygame.K_ESCAPE:
                    pausado = not pausado
                    efecte_pausa.play()
                    efecte_pausa.set_volume(0.3)
                elif event.key == pygame.K_SPACE and not pausado:
                    player.shoot()
        if pausado:
            screen.blit(background3 , (0,0))
            draw_text(screen, "JOC EN PAUSA", font_pause, YELLOW, 170, 150)
            draw_text(screen, "Prem ESC de nou per reanudar", font_standard, YELLOW, 230, 300)
            max_score_text = font_standard.render("Puntuació Màxima: " + str(max_score), True, AMARILLO_LIMA)
            score_text = font_standard.render("Puntuació: " + str(score), True, AMARILLO_LIMA)
            difficulty_text = font_standard.render("Dificultat: " + str(difficulty_level), True, AMARILLO_LIMA)
            lives_text = font_standard.render("Vides: " + str(lives), True, AMARILLO_LIMA)
            screen.blit(max_score_text,(10,10))
            screen.blit(score_text, (10, 40))
            screen.blit(difficulty_text, (10, 70))
            screen.blit(lives_text, (10, 100))
            pygame.display.flip()
            while pausado:  # Esperar fins que es despausi
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pausado = False  # Reprendre el joc
                        efecte_reanudar.play()
                        efecte_reanudar.set_volume(0.3)
            continue


            # Incrementar la dificultat cada 15 segons
        current_time = pygame.time.get_ticks()
        if current_time - last_difficulty_update_time >= 10000:
            difficulty_level += 1
            last_difficulty_update_time = current_time
            spawn_interval = max(500, 1500 - difficulty_level * 100)
            pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)
        # Actualitzar els sprites
        all_sprites.update()
        # Comprovar col·lisions
        if pygame.sprite.spritecollideany(player, obstacles):
            lives -= 1
            efecte_colisio.play()
            efecte_colisio.set_volume(0.1)
            if lives > 0:
                # Reinicialitzar la posició del jugador i esborrar els obstacles
                player.rect.center = (100, HEIGHT // 2)
                for obs in obstacles:
                    obs.kill()
            else:
                game_state = "game_over"
        collided_powerup = pygame.sprite.spritecollideany(player, powerups)
        if collided_powerup:
            player.increase_speed()
            efecte_powerup.play()
            efecte_powerup.set_volume(0.1)
            collided_powerup.kill()
            powerup_message = "SPEED UP!!"
            powerup_message_time = pygame.time.get_ticks()
        if powerup_message and pygame.time.get_ticks() - powerup_message_time < 2000:  # Mostrar por 2 segundos
            powerup_text = font_powerups.render(powerup_message, True, WHITE)
            screen.blit(powerup_text, (350, 150))
        else:
            powerup_message = ""  # Borrar el mensaje después de 2 segundos
        # Detectar colisions entre bales y obstácles
        for bullet in bullets:
            hit_obstacle = pygame.sprite.spritecollideany(bullet, obstacles)
            if hit_obstacle:
                bullet.kill()  # Eliminar la bala
                hit_obstacle.kill()  # Eliminar el obstáculo
                score += 1  # Aumentar la puntuación

                explosion = Explosion(hit_obstacle.rect.centerx, hit_obstacle.rect.centery)
                all_sprites.add(explosion)
                efecte_destruccio_roca.play()
                efecte_destruccio_roca.set_volume(0.1)

        # Detectar colisions entre jugador i healing
        collided_healing  = pygame.sprite.spritecollideany(player, healings)
        if collided_healing:
            efecte_healup.set_volume(0.1)
            efecte_healup.play()
            add_life()
            collided_healing.kill()


        pygame.display.flip()
    return score

# ========================
# Funció per mostrar la pantalla de Game Over
# ========================

def show_game_over(final_score):
    """Mostra la pantalla de Game Over amb la puntuació final i espera per reiniciar."""
    global max_score
    screen.blit(background4,(0,0))
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
            if final_score > max_score:
                max_score = final_score
        draw_text(screen, "Game Over!", font_pause, RED, 200, 150)
        draw_text(screen, "Puntuació Màxima: " + str(max_score), font_standard, YELLOW, 290, 350)
        draw_text(screen, "Puntuació Final: " + str(final_score), font_standard, YELLOW, 298, 400)
        draw_text(screen, "Prem qualsevol tecla per reiniciar", font_standard, YELLOW, 230, 450)
        pygame.display.flip()


# ========================
# Bucle principal del programa
# ========================

while True:
    show_menu()  # Mostrar menú d'inici
    final_score = game_loop()  # Executar la partida
    show_game_over(final_score)  # Mostrar pantalla de Game Over i esperar reinici
# Mostrar pantalla de Game Over i esperar reinici
