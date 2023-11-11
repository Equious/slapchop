from pydub import AudioSegment
import os


# create a directory to store the output chunks
output_dir = "output_chunks"


def cut(cutList, input_file, output_dir="chunks"):
    # Create an AudioSegment object from the input file
    audio = AudioSegment.from_mp3(input_file)

    # Ensure that output_dir exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over the timestamps in cutList and create audio chunks
    for i, timestamp in enumerate(cutList):
        # Assume that the timestamp is a string in the format "MM:SS"
        # Convert the timestamp into milliseconds
        minutes, seconds = map(int, timestamp.split(":"))
        start_time = (minutes * 60 + seconds) * 1000

        # Determine the end time for the chunk
        # If this is the last timestamp in the list, set end_time to the length of the audio
        if i + 1 == len(cutList):
            end_time = len(audio)
        else:
            # Otherwise, set end_time to the next timestamp in the list
            next_minutes, next_seconds = map(int, cutList[i + 1].split(":"))
            end_time = (next_minutes * 60 + next_seconds) * 1000

        # Create a new AudioSegment object for the chunk
        chunk = audio[start_time:end_time]

        # Generate a filename for the chunk
        output_file = f"{output_dir}/chunk{i}.mp3"

        # Export the chunk to a new .mp3 file
        chunk.export(output_file, format="mp3")
        print(f"Chop number {i+1} complete!")
