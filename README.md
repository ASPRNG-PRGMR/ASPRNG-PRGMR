<picture>
  <source media="(max-width: 600px)" srcset="assets/header-mobile.svg">
  <img src="about_me.svg" width="100%" alt="Arnab Ranjan Sikdar — I build across the whole stack. Firmware, systems, vision, robotics.">
</picture>

I build where software meets the physical world: Linux talking to unsupported hardware, vision running on microcontrollers, and robots learning to move. I like understanding the entire path — from a sensor reading or a byte on the wire to the thing you see on screen.

**Rust · C / C++ · Python · Embedded C** &nbsp; / &nbsp; Linux · ESP32 · STM32 · GPU rendering

[Email](mailto:arnabranjan.sikdar@gmail.com) &nbsp; ↗ &nbsp; [LinkedIn](https://www.linkedin.com/in/arnab-ranjan-sikdar-0a634933a/)

## Selected builds

Six projects, from the wire protocol to the pixels. Open a card to explore the code.

<p align="center">
  <a href="https://github.com/ASPRNG-PRGMR/hashi"><img src="assets/hashi.svg" width="340" alt="HASHI — an iPad as a USB extended display for Linux, with touch input. Python, C++, Rust. Hardware-tested alpha."></a>
  <a href="https://github.com/ASPRNG-PRGMR/kage"><img src="assets/kage.svg" width="340" alt="KAGE — OLED-aware text rendering and physical subpixel simulation. Rust, OpenGL, Vulkan. Research sandbox."></a>
  <a href="https://github.com/ASPRNG-PRGMR/senpai"><img src="assets/senpai.svg" width="340" alt="SENPAI — a native document reader with a Rust core and Poppler rendering. Rust, C++, egui. Early development."></a>
  <a href="https://github.com/ASPRNG-PRGMR/EdgeCV"><img src="assets/edgecv.svg" width="340" alt="EdgeCV — offline image classification on ESP32 camera hardware. ESP32, TensorFlow Lite Micro. Classifier running on hardware."></a>
  <a href="https://github.com/ASPRNG-PRGMR/EdgeRover"><img src="assets/edgerover.svg" width="340" alt="EdgeRover — a four-wheel rover with ESP-NOW control and AprilTag follower firmware. ESP32, C++, control systems. Bench testing pending."></a>
  <a href="https://github.com/ASPRNG-PRGMR/bhukavach"><img src="assets/bhukavach.svg" width="340" alt="BhuKavach — reconstructing ground deformation from a mesh of tilt sensors. Python, MEMS, telemetry. Simulation validated; not field validated."></a>
</p>

## Also on the workbench

<details>
<summary><b>01 / Linux, hardware &amp; infrastructure</b></summary>

| Project | What I'm building |
| :--- | :--- |
| [PointerForce](https://github.com/ASPRNG-PRGMR/PointerForce) | Per-device Linux input mapping with a live control plane. |
| [PinchKey](https://github.com/ASPRNG-PRGMR/PinchKey) | Native browser pinch zoom from a mouse wheel, through a virtual touchpad. |
| [OMEN RGB](https://github.com/ASPRNG-PRGMR/omen-rgb-keyboard) | A Linux kernel driver for HP OMEN four-zone keyboard lighting, inspired by `hp-omen-linux-module`. |
| [HomeNAS](https://github.com/ASPRNG-PRGMR/HomeNAS) | A self-hosted NAS with audit logging, attack detection, and an investigation console. |
| [HeteroWise](https://github.com/ASPRNG-PRGMR/HeteroWise) | Energy-aware workload placement across AMD CPU, GPU, and NPU targets. |

</details>

<details>
<summary><b>02 / Embedded systems, sensing &amp; control</b></summary>

| Project | What I'm building |
| :--- | :--- |
| [Green Dot](https://github.com/ASPRNG-PRGMR/greenDot) | ESP32 attitude-control firmware and an ESP-NOW hand controller; hardware validation pending. |
| [TEAM-SILICA](https://github.com/ASPRNG-PRGMR/TEAM-SILICA) | A bare-metal STM32 motor-control ECU with explicit states and emergency handling. |
| [VoltGuard](https://github.com/ASPRNG-PRGMR/smart_meter) | Multi-sensor tamper detection, encrypted meter telemetry, and a monitoring dashboard. |
| [SemantiCAN](https://github.com/ASPRNG-PRGMR/SemantiCAN) | Semantic anomaly detection in simulated vehicle telemetry using rules and a local LSTM. |
| [CSI Project](https://github.com/ASPRNG-PRGMR/csi_project) | Wi-Fi channel-state acquisition and visualization with Raspberry Pi / Nexmon and ESP32. |

</details>

<details>
<summary><b>03 / Applied vision &amp; team builds</b></summary>

| Project | What I'm building |
| :--- | :--- |
| [ANAJ-AI](https://github.com/ASPRNG-PRGMR/ANAJ-AI) | Crop-disease inference split across an ESP32-S3-CAM and Arduino Uno; hardware integration in progress. |
| [SHUWA](https://github.com/ASPRNG-PRGMR/shuwa) | Sign-language recognition with an ESP32 camera feed, PC-side landmarks, and temporal modeling. |
| [Binary Bin / nullVoid](https://github.com/ASPRNG-PRGMR/TEAM-nullVoid) | A smart waste-sorting bin. Team build: **3rd place**, four-hour Buildathon 2026. |

</details>

<details>
<summary><b>04 / Forks &amp; upstream tools I explore</b></summary>

My [OMEN Space fork](https://github.com/ASPRNG-PRGMR/omen-space) builds on [yunusemreyl/omen-space](https://github.com/yunusemreyl/omen-space), a native Linux control center for HP laptops.

The wider workbench also includes upstream checkouts of [Gaze](https://github.com/GunduLabs/gaze), [RealSense SDK](https://github.com/realsenseai/librealsense), [AprilTag](https://github.com/AprilRobotics/apriltag), [AprilTag for ESP32](https://github.com/raspiduino/apriltag-esp32), [TensorRT](https://github.com/NVIDIA/TensorRT), and [Booster train](https://github.com/BoosterRobotics/booster_train). These are other teams' projects, explored alongside my own work.

</details>

---

<p align="center"><sub>Understand the hardware. Trace the signal. Build the whole thing.</sub></p>

<!-- Artwork is local, self-contained SVG. Edit scripts/build_assets.py and run
     python3 scripts/build_assets.py to regenerate it. See CONTRIBUTING.md. -->
