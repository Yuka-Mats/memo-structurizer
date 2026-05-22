FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY web/frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy source
COPY web/frontend ./

# Expose port
EXPOSE 5173

# Run dev server
CMD ["npm", "run", "dev"]
