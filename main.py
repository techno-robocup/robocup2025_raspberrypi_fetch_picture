import modules.uart
import modules.camera
import modules.log
from modules.uart import Message
import traceback
import sys
import math
import time

Rescue_Camera = modules.camera.Camera(
    PORT=modules.settings.RESCUE_CAMERA_PORT,
    controls=modules.settings.RESCUE_CAMERA_CONTROLS,
    size=modules.settings.RESCUE_CAMERA_SIZE,
    formats=modules.settings.RESCUE_CAMERA_FORMATS,
    lores_size=modules.settings.RESCUE_CAMERA_LORES_SIZE,
    pre_callback_func=modules.settings.RESCUE_CAMERA_PRE_CALLBACK_FUNC)

try:
  Rescue_Camera.start_cam()
  
  while True:
    try:
      pass
    except KeyboardInterrupt:
      print("Ending")
      break
    except Exception as e:
      modules.log.error(traceback.format_exc())
      modules.log.error(e)
      time.sleep(1)
finally:
  Rescue_Camera.stop_cam()
