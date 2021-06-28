from game.action import Action
from game.output_service import OutputService

# TODO: Define the DrawActorsAction class here
class DrawActorsAction(Action):
	
	def __init__(self, OutputService):
		self.output_service = OutputService
				
	def execute(self, cast):
		self.output_service.clear_screen()
		for tag in cast:
			self.output_service.draw_actors(cast[tag])
		self.output_service.flush_buffer()
		
	