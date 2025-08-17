import "./style.css";

export function Loader() {
  return <span className="loader"></span>;
}

export function SkeletonLoader() {
  return <div className="skeleton-loader" />;
}

export function ShimmerLoader() {
  return <div className="card shimmer-loader" />;
}
