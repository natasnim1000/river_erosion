# 🚀 Streamlit Cloud Deployment Guide

## Quick Deploy to Streamlit Cloud (Free)

### Step 1: Prepare Your Repository

1. **Create a GitHub account** (if you don't have one)
   - Go to [github.com](https://github.com)
   - Sign up for free

2. **Create a new repository**
   - Name it: `riverbank-adaptation-predictor`
   - Make it public
   - Don't add README (we already have one)

### Step 2: Upload Files to GitHub

Upload these files to your repository:
- `app.py`
- `train_and_save_model.py`
- `requirements.txt`
- `README.md`
- `riverbank_with_indices.csv`

**Important:** You also need to upload the model files:
- `best_model.pkl`
- `scaler.pkl`
- `label_encoders.pkl`
- `target_encoder.pkl`
- `model_metadata.pkl`

*First run `train_and_save_model.py` locally to generate these files, then upload them.*

### Step 3: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "Sign in with GitHub"
   - Authorize Streamlit

2. **Create New App**
   - Click "New app"
   - Select your repository: `riverbank-adaptation-predictor`
   - Main file path: `app.py`
   - Click "Deploy!"

3. **Wait for Deployment**
   - Streamlit will install dependencies
   - Takes 2-5 minutes
   - You'll get a public URL like: `https://your-app-name.streamlit.app`

### Step 4: Share Your App

Your app is now live! Share the URL with:
- Your supervisor
- Team members
- Stakeholders

## 📝 Notes

### File Size Limits
- Streamlit Cloud has a 1GB limit
- Model files should be under 100MB
- CSV dataset should be fine

### Free Tier Limits
- 1 private app OR 3 public apps
- Perfect for this use case
- No credit card required

### Updates
When you push changes to GitHub:
1. Streamlit detects changes
2. Automatically redeploys
3. Takes a few minutes

### Alternative: Use Git LFS for Large Files

If model files are too large (>100MB), use Git Large File Storage:

```bash
# Install Git LFS
git lfs install

# Track .pkl files
git lfs track "*.pkl"

# Commit and push
git add .gitattributes
git add *.pkl
git commit -m "Add model files"
git push
```

## 🔒 Security Considerations

### For Production Use:
1. **Environment Variables**
   - Store sensitive data in Streamlit secrets
   - Create `.streamlit/secrets.toml`

2. **Access Control**
   - Use Streamlit authentication
   - Or deploy on private server

3. **Data Privacy**
   - Ensure dataset doesn't contain PII
   - Follow data protection regulations

## 🎯 Best Practices

1. **Test Locally First**
   ```powershell
   streamlit run app.py
   ```

2. **Check Requirements**
   - Ensure all packages are listed
   - Test with clean environment

3. **Monitor Usage**
   - Streamlit Cloud provides analytics
   - Track visitors and errors

4. **Regular Updates**
   - Keep dependencies updated
   - Retrain model with new data

## 📞 Support

### Streamlit Community
- [Documentation](https://docs.streamlit.io)
- [Community Forum](https://discuss.streamlit.io)
- [Discord](https://discord.gg/streamlit)

### Common Issues

**App won't start:**
- Check requirements.txt
- View deployment logs
- Verify all files uploaded

**Model not found:**
- Ensure .pkl files uploaded
- Check file paths in app.py

**Slow performance:**
- Optimize model size
- Use caching (@st.cache_resource)
- Consider upgrading plan

## ✅ Deployment Checklist

- [ ] All files uploaded to GitHub
- [ ] Model files (.pkl) generated and uploaded
- [ ] requirements.txt is complete
- [ ] App runs locally without errors
- [ ] Streamlit Cloud app created
- [ ] Deployment successful
- [ ] App tested online
- [ ] URL shared with team

---

**Estimated Time:** 15-30 minutes for first deployment

**Cost:** FREE (Streamlit Community Cloud)

**Public URL:** You'll get a permanent link to share!
