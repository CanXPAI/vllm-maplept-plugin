# MaplePT vLLM Plugin

**Author:** [CanXP AI](https://canxp.ai)  
**License:** MIT  
**Repository:** [CanXPAI/vllm_maplept_plugin](https://github.com/CanXPAI/vllm_maplept_plugin)

## Overview

The **MaplePT vLLM Plugin** extends the [vLLM](https://github.com/vllm-project/vllm) inference engine to support **MaplePT** models — a series of **sovereign Canadian-tuned language models** built by [CanXP AI](https://canxp.ai).

This Plugin is needed to support our MaplePT model hosted via vllm on [Hugging Face](https://huggingface.co/canxp-ai/canxpai-maplept-mini-v1).

MaplePT models are derived from **Phi-3** architecture and fine-tuned for Canadian language, policy, and context alignment.  
This plugin provides compatibility patches that allow vLLM to load, alias, and serve MaplePT weights seamlessly as Phi-compatible models.

## ✨ Features

- ✅ Registers **MaplePT** architecture as a **Phi3-compatible backend**  
- ✅ Aliases weight prefixes (`model.* → model.model.*`) for safe loading  
- ✅ Patches `safetensors` loader for multi-process inference  
- ✅ Enables **OpenAI-compatible API serving** via vLLM  
- ✅ Fully self-contained — no vLLM source modification required  

---

## 🧩 Installation

Clone the repository:

```bash
git clone https://github.com/CanXPAI/vllm_maplept_plugin.git
cd vllm_maplept_plugin

