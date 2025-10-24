from setuptools import setup, find_packages

setup(
    name="vllm_maplept_plugin",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "vllm.model_executor.models": [
            # Register MaplePT architecture as compatible with Phi-3
            "maplept = vllm_maplept_plugin.maplept_model:Phi3ForCausalLM",
        ],
    },
    install_requires=[
        "vllm>=0.10.0",
        "transformers",
        "safetensors",
    ],
    description="vLLM plugin registering MaplePT as a Phi-3 compatible model with checkpoint key aliasing.",
    author="CanXP AI",
    license="MIT",
)
