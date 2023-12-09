import asyncio
import websockets
import serial
import pygame

async def receive_and_send():
    async with websockets.connect("ws://localhost:3033") as websocket:
        print("WebSocket connection established")

        # Initialize serial communication with Arduino
        arduino = serial.Serial('/dev/tty.usbmodem1101', 9600)  # Use the correct serial port and baud rate

        # Initialize pygame mixer
        pygame.mixer.init()

        # Variable to store the last played digit
        last_played_digit = None

        while True:
            message = await websocket.recv()
            print("Received data from server:", message)

            arduino.write(message.encode())  # Send message with newline character
            
            # Dictionary mapping integer values to audio file paths
            audio_files = {
                1: 'audio-files/1.wav',
                2: 'audio-files/2.wav',
                3: 'audio-files/3.wav',
                4: 'audio-files/4.wav',
                5: 'audio-files/5.wav'
            }

            # Assuming message is a string like 'data=3'
            try:
                # Extract numeric part from the message
                numeric_value = int(message.split('=')[1])

                # Check if the numeric value is in the dictionary and different from the last played digit
                if numeric_value in audio_files and numeric_value != last_played_digit:
                    # Load and play the corresponding audio file
                    pygame.mixer.Sound(audio_files[numeric_value]).play()
                    # Update the last played digit
                    last_played_digit = numeric_value
                else:
                    print("digit unchanged")
            except (ValueError, IndexError):
                print("Invalid message format")
            
asyncio.get_event_loop().run_until_complete(receive_and_send())
