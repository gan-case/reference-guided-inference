import gradio as gr

def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)

demo.launch(share=True)   

"""
test_opts.exp_dir='output'
    test_opts.checkpoint_path='checkpoint/sam_ffhq_aging.pt'
    test_opts.data_path='reference'
    test_opts.couple_outputs=False
    test_opts.resize_outputs=False
    test_opts.test_batch_size=4
    test_opts.test_workers=4
    test_opts.n_images=None
    test_opts.n_outputs_to_generate=5
    test_opts.ref_images_paths_file='ref.txt'
    test_opts.target_age='50,60,70,80'
    test_opts.latent_mask='8,9'
    test_opts.mix_alpha=None
"""