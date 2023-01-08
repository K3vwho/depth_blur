nputs = gr.inputs.Image(type='pil', label="Original Image")
outputs = gr.outputs.Image(type="pil", label="Output Image")

title = "MiDaS"
description = "Gradio demo for MiDaS v2.1 which takes in a single image for computing relative depth. To use it, simply upload your image, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1907.01341v3'>Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer</a> | <a href='https://github.com/intel-isl/MiDaS'>Github Repo</a></p>"

examples = [
    ["turtle.jpg"],
    ["lions.jpg"]
]

gr.Interface(depth, inputs, outputs, title=title, description=description, article=article,
             examples=examples, analytics_enabled=False).launch(enable_queue=True, cache_examples=True)
