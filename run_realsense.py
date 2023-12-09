# import pyrealsense2 as rs
# import torch
# import numpy as np
# import cv2

# # Configure depth and color streams
# pipeline = rs.pipeline()

# width = 640
# height = 360


# config = rs.config()
# config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)
# config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, 30)

# # Start streaming
# profile = pipeline.start(config)

# # rs.align allows us to perform alignment of depth frames to others frames
# # The "align_to" is the stream type to which we plan to align depth frames.
# align_to = rs.stream.color
# align = rs.align(align_to)

# try:
#     while True:

#         # Wait for a coherent pair of frames: depth and color
#         frames = pipeline.wait_for_frames()

#         aligned_frames = align.process(frames)
#         color_frame = aligned_frames.get_color_frame()
#         depth_frame = aligned_frames.get_depth_frame() 

#         # Validate that both frames are valid
#         if not depth_frame or not color_frame:
#             continue

#         # Convert frames to numpy arrays
#         color_image = np.asanyarray(color_frame.get_data())
#         depth_image = np.asanyarray(depth_frame.get_data())
#         depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.08), cv2.COLORMAP_JET)


#         # Stack both images horizontally
#         images = np.hstack((color_image, depth_colormap))

#         # Show images
#         cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
#         cv2.imshow('RealSense', images)
#         cv2.waitKey(1)

# finally:
#     # Stop streaming
#     pipeline.stop()


import pyrealsense2 as rs
import numpy as np
import cv2

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
profile = pipeline.start(config)

# rs.align allows us to perform alignment of depth frames to others frames
# The "align_to" is the stream type to which we plan to align depth frames.
align_to = rs.stream.color
align = rs.align(align_to)

def resize_with_padding(img, target_size=(320, 320)):
    h, w = img.shape[:2]
    scale = min(target_size[0] / h, target_size[1] / w)
    new_h, new_w = int(h * scale), int(w * scale)
    resized_img = cv2.resize(img, (new_w, new_h))

    top = (target_size[0] - new_h) // 2
    bottom = target_size[0] - new_h - top
    left = (target_size[1] - new_w) // 2
    right = target_size[1] - new_w - left

    return cv2.copyMakeBorder(resized_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

try:
    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()

        # Validate that both frames are valid
        if not depth_frame or not color_frame:
            continue

        # Convert frames to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.08), cv2.COLORMAP_JET)

        # Resize with padding
        color_image_padded = resize_with_padding(color_image)
        depth_colormap_padded = resize_with_padding(depth_colormap)

        # Show images in separate windows
        cv2.namedWindow('RealSense Color', cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow('RealSense Depth', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense Color', color_image_padded)
        cv2.imshow('RealSense Depth', depth_colormap_padded)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Stop streaming
    pipeline.stop()
    cv2.destroyAllWindows()

