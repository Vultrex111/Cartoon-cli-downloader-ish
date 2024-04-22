import subprocess
import os

def get_file_size(file_path):
    try:
        result = subprocess.run(['ffmpeg', '-i', file_path], stderr=subprocess.PIPE, universal_newlines=True)
        output = result.stderr
        # Extracting file size from ffmpeg output
        size_index = output.find("Duration: ")
        if size_index != -1:
            size_str = output[size_index:]
            size_str = size_str.split(",")[1]
            size = size_str.split()[1]
            return size
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None
    except FileNotFoundError:
        print("Error: ffmpeg command not found. Please ensure ffmpeg is installed and in your PATH.")
        return None

def download_with_ffmpeg(link, filename):
    try:
        subprocess.run(['ffmpeg', '-i', link, '-c', 'copy', filename + '.ts'], check=True)
        print("Download completed successfully.")

        ts_file_path = filename + '.ts'
        ts_file_size = get_file_size(ts_file_path)
        if ts_file_size:
            print(f"File size: {ts_file_size}")

        convert_to_mp4 = input("Convert .ts file to .mp4? (Y/N): ").strip().lower()
        if convert_to_mp4 == 'y':
            subprocess.run(['ffmpeg', '-i', ts_file_path, filename + '.mp4'], check=True)
            print("Conversion to .mp4 completed successfully.")
            mp4_file_size = get_file_size(filename + '.mp4')
            if mp4_file_size:
                print(f"File size after conversion: {mp4_file_size}")
        else:
            print("Conversion to .mp4 skipped.")
        
        # Cleanup intermediate .ts file
        os.remove(ts_file_path)
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: ffmpeg command not found. Please ensure ffmpeg is installed and in your PATH.")

if __name__ == "__main__":
    link = input("Enter the link: ")
    filename = input("Enter the filename (without extension): ")
    download_with_ffmpeg(link, filename)

