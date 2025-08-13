# Security Implementation

This document describes the security measures implemented in the Account Service to protect against common web vulnerabilities and CORS attacks.

## Security Headers (Flask-Talisman)

The service uses Flask-Talisman to automatically add security headers to all HTTP responses:

### Implemented Security Headers

- **X-Content-Type-Options**: Prevents MIME type sniffing
- **X-Frame-Options**: Prevents clickjacking attacks
- **X-XSS-Protection**: Enables browser's XSS filtering
- **Strict-Transport-Security**: Enforces HTTPS connections
- **Content-Security-Policy**: Controls resource loading
- **Referrer-Policy**: Controls referrer information

### Content Security Policy (CSP)

The CSP is configured with the following restrictions:
- `default-src`: Only allows resources from the same origin
- `script-src`: Allows scripts from same origin and inline scripts
- `style-src`: Allows styles from same origin and inline styles
- `img-src`: Allows images from same origin, data URIs, and HTTPS sources
- `font-src`: Only allows fonts from same origin
- `connect-src`: Only allows connections to same origin
- `frame-ancestors`: Prevents embedding in iframes
- `base-uri`: Restricts base URI to same origin
- `form-action`: Restricts form submissions to same origin

## CORS Policy (Flask-CORS)

Cross-Origin Resource Sharing is configured to allow controlled access from other domains:

### CORS Configuration

- **Origins**: Configurable via `CORS_ORIGINS` environment variable (defaults to `*`)
- **Methods**: GET, POST, PUT, DELETE, OPTIONS
- **Headers**: Content-Type, Authorization, X-Requested-With
- **Exposed Headers**: Content-Type, X-Total-Count
- **Credentials**: Supported for authenticated requests
- **Max Age**: 1 hour cache for preflight requests

### Environment Variables

Configure security settings using these environment variables:

```bash
# Force HTTPS (default: false)
TALISMAN_FORCE_HTTPS=true

# CORS Origins (comma-separated, default: *)
CORS_ORIGINS=https://example.com,https://app.example.com

# Secret Key for session management
SECRET_KEY=your-secure-secret-key
```

## Testing Security Implementation

Use the provided test script to verify security headers and CORS policies:

```bash
python test_security.py
```

The script will test:
1. Security headers on all responses
2. CORS preflight requests
3. CORS actual requests

## Security Best Practices

1. **Always use HTTPS in production** - Set `TALISMAN_FORCE_HTTPS=true`
2. **Restrict CORS origins** - Limit `CORS_ORIGINS` to trusted domains
3. **Use strong secret keys** - Generate cryptographically secure `SECRET_KEY`
4. **Regular security updates** - Keep dependencies updated
5. **Monitor security headers** - Verify headers are present in production

## Compliance

This implementation helps meet security requirements for:
- OWASP Top 10 security risks
- PCI DSS compliance
- SOC 2 security controls
- GDPR data protection requirements

## Troubleshooting

### Common Issues

1. **CORS errors in browser**: Check `CORS_ORIGINS` configuration
2. **Mixed content warnings**: Ensure `TALISMAN_FORCE_HTTPS` is set
3. **Security headers missing**: Verify Flask-Talisman is properly initialized

### Debug Mode

For development, you can temporarily disable strict security:

```python
# In development only
app.config['TALISMAN_FORCE_HTTPS'] = False
app.config['CORS_ORIGINS'] = ['*']
```

**Warning**: Never use these settings in production! 