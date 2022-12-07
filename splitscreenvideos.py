#pip install moviepy

from moviepy.editor import VideoFileClip, clips_array

length = 2

clip1 = VideoFileClip("").sublicp(0, 0 +length).margin(0)
clip2 = VideoFileClip("").sublicp(0, 0 +length).margin(0)
clip3 = VideoFileClip("").sublicp(0, 0 +length).margin(0)
clip4 = VideoFileClip("").sublicp(0, 0 +length).margin(0)

combined = clips_array([[clip1, clip2],
                        [clip3, clip4]])

combined.write_videofile("test.mp4")