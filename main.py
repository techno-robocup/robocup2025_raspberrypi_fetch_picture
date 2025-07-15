import modules.uart
import modules.camera
import modules.log
from modules.uart import Message
import traceback
import sys
import math
import time

Rescue_Camera = modules.camera.Camera(
    PORT=modules.settings.Rescue_Camera_PORT,
    controls=modules.settings.Rescue_Camera_Controls,
    size=modules.settings.Rescue_Camera_size,
    formats=modules.settings.Rescue_Camera_formats,
    lores_size=modules.settings.Rescue_Camera_lores_size,
    pre_callback_func=modules.settings.Rescue_Camera_Pre_Callback_func)

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
