"""
MaplePT vLLM Plugin — final version
Makes MaplePT load using the Phi-3 runner and patches safetensors key names.
"""
from vllm.model_executor.models.registry import ModelRegistry
from vllm.model_executor.models.phi3 import Phi3ForCausalLM

# Register MaplePT as a Phi-3 compatible architecture
ModelRegistry.register_model("MaplePTForCausalLM", Phi3ForCausalLM)
print("✅ MaplePTForCausalLM → Phi3ForCausalLM registered")

# Patch safetensors loader so keys like model.* also work
try:
    from safetensors import torch as st
    orig = st.load_file

    def patched_load(path, device=None):
        t = orig(path, device=device)
        added = {
            f"model.model.{k[len('model.'):]}" : v
            for k, v in t.items()
            if k.startswith("model.") and not k.startswith("model.model.")
        }
        if added:
            t.update(added)
            print(f"🩹 MaplePT alias: added {len(added)} model.model.* keys (from {path})")
        return t

    st.load_file = patched_load
    print("✅ Safetensors alias patch active")
except Exception as e:
    print(f"⚠️ Alias patch failed: {e}")

print("✅ MaplePT vLLM plugin initialized")
