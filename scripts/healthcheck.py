#!/usr/bin/env python3
import sys
import socket
import argparse
from typing import Tuple, Optional

def check_port(host: str, port: int, timeout: int = 5) -> Tuple[bool, Optional[str]]:
    """Check port"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            return True, None
        else:
            return False, f"Port {port} is closed"
    except socket.gaierror:
        return False, f"Hostname {host} could not be resolved"
    except socket.timeout:
        return False, f"Connection to {host}:{port} timed out"
    except Exception as e:
        return False, str(e)

def check_postgres(host: str, port: int = 5432) -> bool:
    """Check PostgreSQL"""
    print(f"🔍 Checking PostgreSQL at {host}:{port}...")
    success, error = check_port(host, port)
    
    if success:
        print(f"  ✅ PostgreSQL is accessible on port {port}")
        try:
            import psycopg2
            print("  ℹ️  psycopg2 is installed, detailed check available")
        except ImportError:
            print("  ⚠️  Install psycopg2 for detailed PostgreSQL checks: pip install psycopg2-binary")
    else:
        print(f"  ❌ PostgreSQL check failed: {error}")
    
    return success

def check_minio(host: str, api_port: int = 9000, console_port: int = 9001) -> bool:
    """Check MinIO"""
    print(f"🔍 Checking MinIO at {host}...")
    
    api_success, api_error = check_port(host, api_port)
    if api_success:
        print(f"  ✅ MinIO API is accessible on port {api_port}")
    else:
        print(f"  ❌ MinIO API check failed: {api_error}")
    
    console_success, console_error = check_port(host, console_port)
    if console_success:
        print(f"  ✅ MinIO Console is accessible on port {console_port}")
    else:
        print(f"  ❌ MinIO Console check failed: {console_error}")
    
    return api_success and console_success

def main():
    parser = argparse.ArgumentParser(
        description="Check TrashScanner infrastructure availability"
    )
    parser.add_argument(
        "--host",
        required=True,
        help="Server hostname or IP address"
    )
    parser.add_argument(
        "--postgres-port",
        type=int,
        default=5432,
        help="PostgreSQL port (default: 5432)"
    )
    parser.add_argument(
        "--minio-port",
        type=int,
        default=9000,
        help="MinIO API port (default: 9000)"
    )
    parser.add_argument(
        "--minio-console-port",
        type=int,
        default=9001,
        help="MinIO Console port (default: 9001)"
    )
    parser.add_argument(
        "--service",
        choices=["all", "postgres", "minio"],
        default="all",
        help="Service to check (default: all)"
    )
    
    args = parser.parse_args()
    
    print(f"🚀 TrashScanner Infrastructure Health Check")
    print(f"📡 Target: {args.host}")
    print("-" * 50)
    
    results = []
    
    if args.service in ["all", "postgres"]:
        results.append(check_postgres(args.host, args.postgres_port))
        print()
    
    if args.service in ["all", "minio"]:
        results.append(check_minio(args.host, args.minio_port, args.minio_console_port))
        print()
    
    print("-" * 50)
    if all(results):
        print("✅ All checks passed!")
        sys.exit(0)
    else:
        print("❌ Some checks failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
