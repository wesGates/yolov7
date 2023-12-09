import pyrealsense2 as rs
import json
import time


# Create a pipeline
pipeline = rs.pipeline()

# Create a config and configure the pipeline to stream
# (Adjust the below line according to your camera's capabilities)
config = rs.config()
# For example, to enable depth stream, you can use: config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start the pipeline
pipe_profile = pipeline.start(config)

# Get the depth sensor's profile
depth_sensor = pipe_profile.get_device().first_depth_sensor()

# Get the range of the visual presets
preset_range = depth_sensor.get_option_range(rs.option.visual_preset)

# Uncomment the below line to print the preset range
print('Preset range: ' + str(preset_range))

# Loop through the presets and set to 'YOLO' if available
for i in range(int(preset_range.max)):
    visual_preset = depth_sensor.get_option_value_description(rs.option.visual_preset, i)
    print('%02d: %s' % (i, visual_preset))
    if visual_preset == "YOLO.json":
        depth_sensor.set_option(rs.option.visual_preset, i)
        break  # Exit the loop after setting the preset


