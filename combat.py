import heapq

class Battle:
    def __init__(self, board):
        self.characters = board.character_positions.keys()
        self.board = board
        self.time = 0.0  # Current battle time in seconds
        self.event_queue = []  # Min-heap to store events

    def schedule_event(self, time, event_type, actor):
        """Schedules an event in the future."""
        heapq.heappush(self.event_queue, (time, event_type, actor))

    def run(self):
        """Runs the battle simulation."""
        # Initialize first auto-attacks for all characters
        for character in self.characters:
            self.schedule_event(self.time + (1 / character.speed), "attack", character)

        # Process events in order of execution time
        while self.event_queue:
            event_time, event_type, actor = heapq.heappop(self.event_queue)
            self.time = event_time  # Advance time
            teams_alive = set(character.team for character in self.characters if character.hp > 0)
            if len(teams_alive) <= 1:
                return teams_alive.pop()
            if event_type == "attack":
                actor.attack(self.board, self.time)
                self.schedule_event(self.time + (1 / actor.speed * actor.speed_multiplier), "attack", actor)

            elif event_type == "cast_ability":
                actor.cast_ability()
            
            # Tick all effects
            #for character in self.characters:
            #    character.tick_effects()

def battle(board):
    battle=Battle(board)
    winner_team = battle.run()
    print(f"\n{winner_team} wins the battle!")