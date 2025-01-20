import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('ErrorBoundary caught an error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h2 style={errorStyle}>Something went wrong. Please try again later.</h2>;
    }
    return this.props.children;
  }
}

const errorStyle = {
  textAlign: 'center',
  color: 'red',
  marginTop: '20px',
};

export default ErrorBoundary;
