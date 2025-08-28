# Pinellas Trail Challenge - Interactive Course Map

An interactive web mapping application for the Pinellas Trail Challenge 46-mile ultramarathon, featuring aid stations, GPS route data, and downloadable resources.

![Pinellas Trail Challenge Logo](ptc.jpg)

## Features

### 🗺️ **Interactive Map**
- **Multiple map styles**: Outdoors, Standard, and Satellite views
- **GPS route visualization**: Complete 46-mile trail displayed as a blue line
- **Auto-fit bounds**: Map automatically centers on the full course
- **Responsive design**: Works seamlessly on desktop, tablet, and mobile

### 📍 **Aid Station Information**
- **32 waypoints** from start to finish with detailed information
- **Color-coded markers**: 
  - 🟢 Green: Start (Mile 0)
  - 🔴 Red: Finish (Mile 46)
  - 🟠 Orange: Official aid stations
  - 🔵 Blue: Trail waypoints
- **Interactive sidebar**: Click any location to fly to it on the map
- **Detailed information**: Descriptions, amenities, timing, and cutoff data

### 📱 **Mobile-Optimized**
- **Sliding sidebar** with hamburger menu on mobile devices
- **Touch-friendly interactions** optimized for phones and tablets
- **Responsive breakpoints** for different screen sizes
- **Auto-close sidebar** when interacting with map

### 📥 **Downloadable Resources**
- **GPX file**: Load the complete route into GPS devices or running apps
- **CSV data**: Aid station information for spreadsheets and planning tools

## Getting Started

### Prerequisites
- A modern web browser
- Local web server (for file access)
- Mapbox access token

### Installation

1. **Clone or download** this repository
2. **Get a Mapbox token**:
   - Sign up at [mapbox.com](https://account.mapbox.com/)
   - Create a new access token
   - Replace `your_mapbox_access_token_here` in `.env` with your token

3. **Start a local server**:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   
   # Using PHP
   php -S localhost:8000
   ```

4. **Open in browser**: Navigate to `http://localhost:8000`

## File Structure

```
pinellas-trail-challenge/
├── index.html              # Main application file
├── ptc.gpx                 # GPS route data (903 track points)
├── ptc-aid-locations.csv   # Aid station and waypoint data
├── ptc.jpg                 # Race logo
├── .env                    # Mapbox access token (not in git)
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Data Sources

### GPS Route (`ptc.gpx`)
- **46-mile route** from St. Petersburg to Tarpon Springs and back
- **903 track points** with precise GPS coordinates
- Generated from the official Pinellas Trail

### Aid Stations (`ptc-aid-locations.csv`)
- **32 locations** including start, finish, aid stations, and waypoints
- **Detailed information**: Mile markers, descriptions, amenities
- **Timing data**: 12-minute pace estimates and cutoff times
- **Logistics**: Drop bag availability, gel stations, parking info

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Mapping**: Mapbox GL JS v3.0.1
- **Responsive Design**: CSS Grid, Flexbox, Media Queries
- **Data Formats**: GPX, CSV
- **Icons**: Inline SVG

## Features Breakdown

### Map Styles
- **Outdoors**: Topographic style perfect for trail visualization
- **Standard**: Clean, minimal style focusing on geography
- **Satellite**: Aerial imagery showing real-world context

### Aid Station Data Fields
- Mile marker position
- Location description
- Aid station availability (Y/N)
- Drop bag support (Y/N)
- HUMA gel availability (Y/N)
- GPS coordinates (lat/lon)
- Approximate address
- Cutoff times
- 12-minute pace arrival estimates

### Mobile Responsive Breakpoints
- **Desktop** (>768px): Full sidebar layout
- **Tablet** (≤768px): Responsive sizing with mobile toggle
- **Phone** (≤480px): Optimized touch interactions and stacked layouts

## Browser Support

- **Chrome**: 88+ ✅
- **Firefox**: 85+ ✅
- **Safari**: 14+ ✅
- **Edge**: 88+ ✅
- **Mobile browsers**: iOS Safari 14+, Chrome Mobile 88+ ✅

## Performance

- **Lightweight**: ~50KB total size (excluding map tiles)
- **Fast loading**: Embedded data, minimal external dependencies
- **Offline-capable**: Downloads work offline once loaded
- **Mobile-optimized**: Touch interactions and responsive images

## Contributing

This is a race-specific application, but improvements are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on multiple devices/browsers
5. Submit a pull request

## Race Information

**Event**: Pinellas Trail Challenge Ultramarathon  
**Distance**: 46 miles  
**Date**: August 30, 2025  
**Course**: Out-and-back on the Pinellas Trail  
**Start/Finish**: St. Petersburg to Tarpon Springs and back to Dunedin

## License

This project is created for the Pinellas Trail Challenge community. The race logo and official data are property of the race organizers.

## Support

For technical issues with this mapping application, please open an issue in this repository.

For race-related questions, contact the official Pinellas Trail Challenge organizers.

---

*Built with ❤️ for the Pinellas Trail Challenge running community*