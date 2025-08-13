#!/usr/bin/env python3
"""
Test script to verify security headers and CORS policies
"""
import requests
import json

def test_security_headers():
    """Test that security headers are properly set"""
    print("Testing Security Headers...")
    
    # Test health endpoint
    response = requests.get("http://localhost:8000/health")
    
    print(f"Status Code: {response.status_code}")
    print("Security Headers:")
    
    # Check for important security headers
    security_headers = [
        'X-Content-Type-Options',
        'X-Frame-Options', 
        'X-XSS-Protection',
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'Referrer-Policy'
    ]
    
    for header in security_headers:
        value = response.headers.get(header)
        if value:
            print(f"  {header}: {value}")
        else:
            print(f"  {header}: NOT SET")
    
    print()

def test_cors_policy():
    """Test CORS policy"""
    print("Testing CORS Policy...")
    
    # Test preflight request
    headers = {
        'Origin': 'http://example.com',
        'Access-Control-Request-Method': 'POST',
        'Access-Control-Request-Headers': 'Content-Type'
    }
    
    response = requests.options("http://localhost:8000/accounts", headers=headers)
    
    print(f"Preflight Status Code: {response.status_code}")
    print("CORS Headers:")
    
    cors_headers = [
        'Access-Control-Allow-Origin',
        'Access-Control-Allow-Methods',
        'Access-Control-Allow-Headers',
        'Access-Control-Max-Age'
    ]
    
    for header in cors_headers:
        value = response.headers.get(header)
        if value:
            print(f"  {header}: {value}")
        else:
            print(f"  {header}: NOT SET")
    
    print()

def test_cors_actual_request():
    """Test actual CORS request"""
    print("Testing Actual CORS Request...")
    
    headers = {
        'Origin': 'http://example.com',
        'Content-Type': 'application/json'
    }
    
    response = requests.get("http://localhost:8000/accounts", headers=headers)
    
    print(f"Actual Request Status Code: {response.status_code}")
    print("CORS Response Headers:")
    
    cors_headers = [
        'Access-Control-Allow-Origin',
        'Access-Control-Allow-Credentials'
    ]
    
    for header in cors_headers:
        value = response.headers.get(header)
        if value:
            print(f"  {header}: {value}")
        else:
            print(f"  {header}: NOT SET")
    
    print()

if __name__ == "__main__":
    print("Security and CORS Test Suite")
    print("=" * 40)
    print()
    
    try:
        test_security_headers()
        test_cors_policy()
        test_cors_actual_request()
        
        print("All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the service.")
        print("Make sure the Flask service is running on localhost:8000")
    except Exception as e:
        print(f"Error during testing: {e}") 