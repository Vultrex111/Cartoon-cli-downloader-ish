import subprocess
import time

def download_with_ffmpeg(link, filename):
    subprocess.run(['ffmpeg', '-i', link, '-c', 'copy', filename + '.ts'])
    convert_to_mp4 = input("Convert .ts file to .mp4? (Y/N): ").strip().lower()
    if convert_to_mp4 == 'y':
        subprocess.run(['ffmpeg', '-i', filename + '.ts', filename + '.mp4'])

if __name__ == "__main__":
    link = input("Enter the link: ")
    time.sleep(2)  # Delay for 2 seconds
    filename = input("Enter the filename (without extension): ")
    download_with_ffmpeg(link, filename)

