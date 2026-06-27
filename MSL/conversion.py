import tensorflow as tf
import os

base = r"D:\User\Documents\#UTM\SEMESTER 6\PSM1\InitialMSL\MSL"
h5_path = os.path.join(base, "msl_model.h5")
saved_model_path = os.path.join(base, "msl_saved_model")
onnx_path = os.path.join(base, "msl_model.onnx")

print("Loading model...")
model = tf.keras.models.load_model(h5_path)
print("Loaded!")

print("Saving as SavedModel...")
model.export(saved_model_path)
print("Saved!")

print("Converting to ONNX...")
os.system(
    f'python -m tf2onnx.convert --saved-model "{saved_model_path}" '
    f'--output "{onnx_path}" --opset 13'
)

print(f"Done! ONNX saved to: {onnx_path}")