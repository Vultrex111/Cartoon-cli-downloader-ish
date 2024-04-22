import subprocess

def download_with_ffmpeg(link, filename):
    subprocess.run(['ffmpeg', '-i', link, '-c', 'copy', filename + '.ts'])
    subprocess.run(['ffmpeg', '-i', filename + '.ts', filename + '.mp4'])

if __name__ == "__main__":
    link = input("Enter the link: ")
    filename = input("Enter the filename (without extension): ")
    download_with_ffmpeg(link, filename)

