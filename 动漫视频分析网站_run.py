#!/usr/bin/env python
"""
动漫视频数据分析平台 - 启动脚本
"""
import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 导入并运行uvicorn
import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("🎬 动漫视频数据分析平台")
    print("=" * 60)
    print(f"\n📂 项目目录: {project_root}")
    print(f"🗄️  数据库: {project_root / 'data' / 'anime_videos.db'}")
    print(f"\n🚀 正在启动服务...\n")
    
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=[str(project_root)],
        log_level="info"
    )
