from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
import asyncio

class HelloBehaviour(OneShotBehaviour):
    async def run(self):
        print("Hello! SPADE agent has started successfully.")
        await self.agent.stop()

class HelloAgent(Agent):
    async def setup(self):
        print("Agent is starting...")
        self.add_behaviour(HelloBehaviour())

async def main():
    agent = HelloAgent(
        "agent1@localhost",
        "password"
    )
    await agent.start()
    await asyncio.sleep(2)
    await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
